import 'package:flutter/material.dart';
import 'package:flutter_osm_plugin/flutter_osm_plugin.dart';
import 'package:flutter_polyline_points/flutter_polyline_points.dart';
import 'package:geolocator/geolocator.dart';

void main() {
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;
  

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  PolylinePoints polylinePoints = PolylinePoints();
  // List<LatLng> polylineCoordinates = [];
  MapController controller = MapController.withUserPosition(
      trackUserLocation: UserTrackingOption(
    enableTracking: true,
    unFollowUser: true,
  ));
  GeoPoint? destinationMarker;
  String totalDistance = "";
  String averageTime = "";
  Card? routeCard;
  bool isDrawRouteButtonClicked = false;

 

  Card createRouteCard(String totalDistance, String averageTime) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(8),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Total Distance: $totalDistance'),
            Text('Average Time: $averageTime'),
          ],
        ),
      ),
    );
  }


  Future<void> drawRouteBetweenUserAndPoint(
      GeoPoint userLocation, GeoPoint destination) async {
    final config = MultiRoadConfiguration(
      startPoint: userLocation,
      destinationPoint: destination,
      roadOptionConfiguration: MultiRoadOption(
        roadColor: Colors.blue, 
      ),
    );

    await controller.drawMultipleRoad([config],
        commonRoadOption: MultiRoadOption(
          roadColor: Colors.red,
        ));
  }

  BottomAppBar buildBottomAppBar() {
  return BottomAppBar(
    child: Padding(
      padding: const EdgeInsets.all(8.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          Expanded(
            child: Text(
              'Total Distance: $totalDistance',
              textAlign: TextAlign.center,
            ),
          ),
          Expanded(
            child: Text(
              'Average Time: $averageTime',
              textAlign: TextAlign.center,
            ),
          ),
        ],
      ),
    ),
  );
}

  var markerMap = <String, String>{};
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) async {
      controller.listenerMapSingleTapping.addListener(() async {
        var position = controller.listenerMapSingleTapping.value;
        if (position != null) {
          await controller.addMarker(position,
              markerIcon: const MarkerIcon(
                icon: Icon(
                  Icons.pin_drop,
                  color: Colors.red,
                  size: 48,
                ),
              ));
          var key = '${position.latitude}_${position.longitude}';
          markerMap[key] = markerMap.length.toString();
        }
        if (destinationMarker != null) {
          await controller.addMarker(destinationMarker!,
              markerIcon: const MarkerIcon(
                icon: Icon(
                  Icons.pin_drop,
                  color: Colors.blue,
                  size: 48,
                ),
              ));
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: null,
      
      body: OSMFlutter(
          controller: controller,
          osmOption: OSMOption(
            userTrackingOption: UserTrackingOption(
              enableTracking: true,
              unFollowUser: false,
            ),
            zoomOption: ZoomOption(
              initZoom: 8,
              minZoomLevel: 3,
              maxZoomLevel: 19,
              stepZoom: 1.0,
            ),
            userLocationMarker: UserLocationMaker(
              personMarker: MarkerIcon(
                icon: Icon(
                  Icons.location_history_rounded,
                  color: Colors.red,
                  size: 48,
                ),
              ),
              directionArrowMarker: MarkerIcon(
                icon: Icon(
                  Icons.double_arrow,
                  size: 48,
                ),
              ),
            ),
            roadConfiguration: RoadOption(
              roadColor: Colors.yellowAccent,
            ),
            markerOption: MarkerOption(
                defaultMarker: MarkerIcon(
              icon: Icon(
                Icons.person_pin_circle,
                color: Colors.blue,
                size: 56,
              ),
            )),
          ),
          onGeoPointClicked: (geoPoint) async {
            var key = '${geoPoint.latitude}_${geoPoint.longitude}';
            const Divider customDivider = Divider(thickness: 1);
            final Text keyText = Text(key);
            Position userLocation = await Geolocator.getCurrentPosition();
            GeoPoint userGeoPoint = GeoPoint(
                latitude: userLocation.latitude,
                longitude: userLocation.longitude);

            if (geoPoint != null) {
              double distanceInMeters = await distance2point(userGeoPoint, geoPoint);
    
              double averageSpeedKmPerHour = 65.0;
              double totalDistanceKm = distanceInMeters / 1000;
              double averageTimeInHours = totalDistanceKm / averageSpeedKmPerHour;
              double averageTimeInSeconds = averageTimeInHours * 60 * 60;
               setState(() {
              totalDistance = "${totalDistanceKm.toStringAsFixed(2)} km";
              averageTime = "${(averageTimeInSeconds / 60).toStringAsFixed(1)} minutes";
              routeCard = createRouteCard(totalDistance, averageTime);
            });

              showModalBottomSheet(
                  context: context,
                  builder: (context) {
                    return Card(
                        child: Padding(
                      padding: const EdgeInsets.all(8),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        crossAxisAlignment: CrossAxisAlignment.start,
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Expanded(
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Text(
                                  'Marked Position',
                                  style: TextStyle(
                                      fontSize: 20,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.red),
                                  
                                ),
                                customDivider,
                                keyText,
                                SizedBox(
                                  height: 10,
                                ),
                                ElevatedButton(
                                    onPressed: () {
                                      setState(() {
                                        isDrawRouteButtonClicked = true;
                                        destinationMarker = geoPoint;
                                      });
                                      controller.addMarker(
                                          geoPoint,
                                          markerIcon: const MarkerIcon(
                                            icon: Icon(
                                              Icons.pin_drop,
                                              color: Colors
                                                  .blue,
                                              size: 48,
                                            ),
                                          ));
                                      drawRouteBetweenUserAndPoint(
                                          userGeoPoint, geoPoint);
                                      Navigator.pop(context);
                                    },
                                    child: Text("draw route")),
                                SizedBox(
                                  height: 10,
                                ),
                                Text("Total Distance: $totalDistance"),
                                Text("Average Time: $averageTime"),
                              ],
                            ),
                          ),
                          GestureDetector(
                            onTap: () => Navigator.pop(context),
                            child: const Icon(Icons.clear),
                          )
                        ],
                      ),
                    ));
                  });
            }
          }),
    bottomNavigationBar: isDrawRouteButtonClicked ? buildBottomAppBar(): null,
    );
  }
}
