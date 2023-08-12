packages/espresso/android/src/main/java/androidx/test/espresso/flutter/exception/NoMatchingWidgetException.java
===============================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.exception;

import androidx.test.espresso.EspressoException;

/**
 * Indicates that a given {@code WidgetMatcher} did not match any widgets in the Flutter UI
 * hierarchy.
 */
public final class NoMatchingWidgetException extends RuntimeException implements EspressoException {

  public NoMatchingWidgetException(String message) {
    super(message);
  }
}


