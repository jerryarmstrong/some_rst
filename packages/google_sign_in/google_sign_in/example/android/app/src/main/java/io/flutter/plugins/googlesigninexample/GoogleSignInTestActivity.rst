packages/google_sign_in/google_sign_in/example/android/app/src/main/java/io/flutter/plugins/googlesigninexample/GoogleSignInTestActivity.java
=============================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlesigninexample;

import androidx.annotation.NonNull;
import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;

// Makes the FlutterEngine accessible for testing.
public class GoogleSignInTestActivity extends FlutterActivity {
  public FlutterEngine engine;

  @Override
  public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {
    super.configureFlutterEngine(flutterEngine);
    engine = flutterEngine;
  }
}


