packages/in_app_purchase/in_app_purchase_android/android/src/test/java/android/text/TextUtils.java
==================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package android.text;

public class TextUtils {
  public static boolean isEmpty(CharSequence str) {
    return str == null || str.length() == 0;
  }
}


