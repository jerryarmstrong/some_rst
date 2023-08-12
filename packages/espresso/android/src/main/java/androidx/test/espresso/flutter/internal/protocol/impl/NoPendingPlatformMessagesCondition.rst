packages/espresso/android/src/main/java/androidx/test/espresso/flutter/internal/protocol/impl/NoPendingPlatformMessagesCondition.java
=====================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.internal.protocol.impl;

/**
 * Represents a condition that waits until there are no pending platform messages in the Flutter's
 * platform channels.
 */
class NoPendingPlatformMessagesCondition extends WaitCondition {

  public NoPendingPlatformMessagesCondition() {
    super("NoPendingPlatformMessagesCondition");
  }
}


