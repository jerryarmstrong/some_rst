packages/espresso/android/src/main/java/androidx/test/espresso/flutter/internal/idgenerator/IdException.java
============================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.internal.idgenerator;

/** Thrown if an ID cannot be generated. */
public final class IdException extends RuntimeException {

  private static final long serialVersionUID = 0L;

  public IdException() {
    super();
  }

  public IdException(String message) {
    super(message);
  }

  public IdException(String message, Throwable throwable) {
    super(message, throwable);
  }

  public IdException(Throwable throwable) {
    super(throwable);
  }
}


