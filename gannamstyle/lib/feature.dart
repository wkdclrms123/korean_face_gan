import 'dart:async';

import 'package:flutter/material.dart';
import 'dart:io';

// for http method
import 'package:http/http.dart' as http;
import 'dart:convert';

// UI
import 'package:flutter_swiper/flutter_swiper.dart';

//Next
import 'package:gannamstyle/result.dart';

class ChooseConvertImageScreen extends StatefulWidget {
  final String imagePath;
  final String gender;
  ChooseConvertImageScreen({Key key, this.imagePath, this.gender}) : super(key: key);

  _ChooseConvertImageScreenState createState() => _ChooseConvertImageScreenState();
}

class _ChooseConvertImageScreenState extends State<ChooseConvertImageScreen> {
  Map<String, dynamic> recogJson;

  @override
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery
        .of(context)
        .size;
    double width = screenSize.width;
    double height = screenSize.height;
    return Scaffold(
        appBar: AppBar(
            backgroundColor: Colors.white,
            title: Text('Choose Convert Image',
                style: TextStyle(
                  color: Colors.black,
                ))),
        // 이미지는 디바이스에 파일로 저장됩니다. 이미지를 보여주기 위해 주어진
        // 경로로 `Image.file`을 생성하세요.
        backgroundColor: Color(0xffF0E5CF),
        body: Swiper(
          itemCount: 3,
          itemBuilder: (BuildContext context, int index) {
            return featureField(width, height, index);
          },
          viewportFraction: 0.8,
          scale: 0.9,
          layout: SwiperLayout.CUSTOM,
          itemHeight: height * 0.7,
          itemWidth: width * 0.9,
          //loop: false,
          control: SwiperControl(),
          pagination: SwiperPagination(),
          customLayoutOption: CustomLayoutOption(startIndex: -1, stateCount: 3)
              .addRotate([-45.0/180, 0.0, 45.0/180]).addTranslate([
            Offset(-370.0, -40.0),
            Offset(0.0, 0.0),
            Offset(370.0, -40.0)
          ]),
        ));
  }

  Widget featureField(double width, double height, int index) {
    return Container(
        color: Color(0xffF7F6F2),
        child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Center(
                  child : Container(
                      padding: new EdgeInsets.only(top: 20.0),
                      child: Text('Korean Face Filter',
                          style: TextStyle(
                            fontSize: 30,
                            color: Color(0xff4B6587),
                          ))
                  )
              ),
              Center(
                  child: SizedBox(
                    width: width * 0.8,
                    height: height * 0.5,
                    child: Image.asset('images/korean_person.jpg'),
                  )
              ),
              Center(
                child: ElevatedButton(
                    onPressed: () async {
                      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                        content: Row(
                          children: [
                            CircularProgressIndicator(),
                            Padding(
                              padding: EdgeInsets.only(left: width * 0.036),
                            ),
                            Text("Loading..."),
                          ],
                        ),
                        duration: Duration(seconds: 10),
                      ));
                      await _postRequest(index);
                    },
                    child: Text('Change Your Face')),
              )
            ]
        )
    );
  }

  _postRequest(int index) async {
    File imageFile = File(widget.imagePath);
    List<int> imageBytes = imageFile.readAsBytesSync();
    String base64Image = base64Encode(imageBytes);
    //teprint(base64Image);
    Uri url;

    //Demo Version
    url = Uri.parse("http://10.0.2.2:8000/post/");

    try {
      http.Response response = await http
          .post(
        url,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        }, // this header is essential to send json data
        body: jsonEncode(
          [
            {
              "image": "$base64Image",
              "gender": widget.gender,
              "feature": index,
            }
          ],
        ),
      )
          .timeout(
        const Duration(seconds: 60),
        onTimeout: () => http.Response('error', 500),
      );
      ScaffoldMessenger.of(context).removeCurrentSnackBar();
      recogJson = await jsonDecode(response.body);
      if (response.statusCode == 200) {
        Navigator.of(context).push(
            MaterialPageRoute(
                builder: (context) => ResultScreen(imagePath: widget.imagePath)));
      }

      print(response.statusCode);
    } on TimeoutException catch (e) {
      print('$e');
    } on Error catch (e) {
      print('Error: $e');
    }
  }
}