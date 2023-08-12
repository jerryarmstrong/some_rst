packages/in_app_purchase/in_app_purchase_android/android/src/test/java/android/util/Log.java
============================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package android.util;

public class Log {
  public static int d(String tag, String msg) {
    System.out.println("DEBUG: " + tag + ": " + msg);
    return 0;
  }

  public static int i(String tag, String msg) {
    System.out.println("INFO: " + tag + ": " + msg);
    return 0;
  }

  public static int w(String tag, String msg) {
    System.out.println("WARN: " + tag + ": " + msg);
    return 0;
  }

  public static int e(String tag, String msg) {
    System.out.println("ERROR: " + tag + ": " + msg);
    return 0;
  }
}


