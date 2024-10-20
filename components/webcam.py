from fasthtml.common import *


def Webcam():
    return Div(
        Video(id="video", autoplay=True),
        Script(
            code="""
            console.log("Hello World!");
            var video = document.querySelector("#video");

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
    })
    .catch(function (error) {
      console.log("Something went wrong!");
    });
}"""
        ),
        style="display: flex; justify-content: center; align-items: center; height: 100vh;",
    )
