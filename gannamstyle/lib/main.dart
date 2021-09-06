import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:gannamstyle/cameraview.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MainPage(),
    );
  }
}

class MainPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('GAN NAM STYLE'),
      ),
      body: Container(
        alignment: Alignment.center,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            //Text("Hello, ${myUser.myUser!.myProfileList[0].nickName}"),
            ElevatedButton(
                onPressed: () async {
                  final camera = await availableCameras();
                  final firstCamera = camera.first;
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => TakePictureScreen(camera: firstCamera)));
                },
                child: Text('Camera')),
          ],
        ),
      ),
    );
  }
}