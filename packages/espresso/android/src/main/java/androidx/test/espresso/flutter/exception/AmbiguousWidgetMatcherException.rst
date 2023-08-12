packages/espresso/android/src/main/java/androidx/test/espresso/flutter/exception/AmbiguousWidgetMatcherException.java
=====================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.exception;

import androidx.test.espresso.EspressoException;

/**
 * Indicates that a {@code WidgetMatcher} matched multiple widgets in the Flutter UI hierarchy when
 * only one widget was expected.
 */
public final class AmbiguousWidgetMatcherException extends RuntimeException
    implements EspressoException {

  public AmbiguousWidgetMatcherException(String message) {
    super(message);
  }
}


