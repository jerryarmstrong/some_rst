packages/espresso/android/src/main/java/androidx/test/espresso/flutter/exception/InvalidFlutterViewException.java
=================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.exception;

import androidx.test.espresso.EspressoException;

/** Indicates that the {@code View} that Espresso operates on is not a valid Flutter View. */
public final class InvalidFlutterViewException extends RuntimeException
    implements EspressoException {

  /** Constructs with an error message. */
  public InvalidFlutterViewException(String message) {
    super(message);
  }
}


