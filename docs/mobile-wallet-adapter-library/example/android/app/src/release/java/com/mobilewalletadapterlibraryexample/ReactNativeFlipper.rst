example/android/app/src/release/java/com/mobilewalletadapterlibraryexample/ReactNativeFlipper.java
==================================================================================================

Last edited: 2023-03-27 15:10:41

Contents:

.. code-block:: java

    /**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * <p>This source code is licensed under the MIT license found in the LICENSE file in the root
 * directory of this source tree.
 */
package com.mobilewalletadapterlibraryexample;

import android.content.Context;
import com.facebook.react.ReactInstanceManager;

/**
 * Class responsible of loading Flipper inside your React Native application. This is the release
 * flavor of it so it's empty as we don't want to load Flipper.
 */
public class ReactNativeFlipper {
  public static void initializeFlipper(Context context, ReactInstanceManager reactInstanceManager) {
    // Do nothing as we don't want to initialize Flipper on Release.
  }
}


