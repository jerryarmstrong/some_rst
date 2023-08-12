packages/google_sign_in/google_sign_in_android/example/android/app/src/androidTest/java/io/flutter/plugins/googlesigninexample/GoogleSignInTest.java
====================================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlesigninexample;

import static org.junit.Assert.assertTrue;

import androidx.test.core.app.ActivityScenario;
import io.flutter.plugins.googlesignin.GoogleSignInPlugin;
import org.junit.Test;

public class GoogleSignInTest {
  @Test
  public void googleSignInPluginIsAdded() {
    final ActivityScenario<GoogleSignInTestActivity> scenario =
        ActivityScenario.launch(GoogleSignInTestActivity.class);
    scenario.onActivity(
        activity -> {
          assertTrue(activity.engine.getPlugins().has(GoogleSignInPlugin.class));
        });
  }
}


