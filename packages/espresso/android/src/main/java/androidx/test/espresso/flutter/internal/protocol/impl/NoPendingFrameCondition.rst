packages/espresso/android/src/main/java/androidx/test/espresso/flutter/internal/protocol/impl/NoPendingFrameCondition.java
==========================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.internal.protocol.impl;

/**
 * Represents a condition that waits until no pending frame is scheduled in the Flutter framework.
 */
class NoPendingFrameCondition extends WaitCondition {

  public NoPendingFrameCondition() {
    super("NoPendingFrameCondition");
  }
}


