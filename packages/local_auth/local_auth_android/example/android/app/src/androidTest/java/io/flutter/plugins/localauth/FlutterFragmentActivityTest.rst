packages/local_auth/local_auth_android/example/android/app/src/androidTest/java/io/flutter/plugins/localauth/FlutterFragmentActivityTest.java
=============================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.localauth;

import androidx.test.rule.ActivityTestRule;
import dev.flutter.plugins.integration_test.FlutterTestRunner;
import io.flutter.embedding.android.FlutterFragmentActivity;
import io.flutter.plugins.DartIntegrationTest;
import org.junit.Rule;
import org.junit.runner.RunWith;

@DartIntegrationTest
@RunWith(FlutterTestRunner.class)
public class FlutterFragmentActivityTest {
  @Rule
  public ActivityTestRule<FlutterFragmentActivity> rule =
      new ActivityTestRule<>(FlutterFragmentActivity.class);
}


