packages/webview_flutter/webview_flutter_android/example/android/app/src/main/java/io/flutter/plugins/webviewflutterexample/DriverExtensionActivity.java
========================================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutterexample;

import androidx.annotation.NonNull;
import io.flutter.embedding.android.FlutterActivity;

public class DriverExtensionActivity extends FlutterActivity {
  @Override
  @NonNull
  public String getDartEntrypointFunctionName() {
    return "appMain";
  }
}


