packages/espresso/android/src/main/java/androidx/test/espresso/flutter/internal/protocol/impl/FlutterProtocolException.java
===========================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.internal.protocol.impl;

/** Represents an exception/error relevant to Dart VM service. */
public final class FlutterProtocolException extends RuntimeException {

  public FlutterProtocolException(String message) {
    super(message);
  }

  public FlutterProtocolException(Throwable t) {
    super(t);
  }

  public FlutterProtocolException(String message, Throwable t) {
    super(message, t);
  }
}


