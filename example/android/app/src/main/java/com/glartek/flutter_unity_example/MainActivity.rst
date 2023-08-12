example/android/app/src/main/java/com/glartek/flutter_unity_example/MainActivity.java
=====================================================================================

Last edited: 2020-08-27 16:54:43

Contents:

.. code-block:: java

    package com.glartek.flutter_unity_example;

import androidx.annotation.NonNull;
import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugins.GeneratedPluginRegistrant;

public class MainActivity extends FlutterActivity {
  @Override
  public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {
    GeneratedPluginRegistrant.registerWith(flutterEngine);
  }
}


