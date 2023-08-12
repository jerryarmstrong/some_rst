packages/google_sign_in/google_sign_in_android/android/src/main/java/io/flutter/plugins/googlesignin/Executors.java
===================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlesignin;

import android.os.Handler;
import android.os.Looper;
import java.util.concurrent.Executor;

/**
 * Factory and utility methods for {@code Executor}.
 *
 * <p>TODO(jackson): If this class is useful for other plugins, consider including it in a shared
 * library or in the Flutter engine
 */
public final class Executors {

  private static final class UiThreadExecutor implements Executor {
    private static final Handler UI_THREAD = new Handler(Looper.getMainLooper());

    @Override
    public void execute(Runnable command) {
      UI_THREAD.post(command);
    }
  }

  /** Returns an {@code Executor} that will post commands to the UI thread. */
  public static Executor uiThreadExecutor() {
    return new UiThreadExecutor();
  }

  // Should never be instantiated.
  private Executors() {}
}


