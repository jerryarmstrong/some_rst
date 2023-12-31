packages/espresso/android/src/main/java/androidx/test/espresso/flutter/api/WidgetAssertion.java
===============================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package androidx.test.espresso.flutter.api;

import android.view.View;
import androidx.test.espresso.flutter.model.WidgetInfo;
import com.google.common.annotations.Beta;

/**
 * Similar to a {@code ViewAssertion}, a {@link WidgetAssertion} is responsible for performing an
 * assertion on a Flutter widget.
 */
@Beta
public interface WidgetAssertion {

  /**
   * Checks the state of the Flutter widget.
   *
   * @param flutterView the Flutter view that this widget lives in.
   * @param widgetInfo the instance that represents a Flutter widget.
   */
  void check(View flutterView, WidgetInfo widgetInfo);
}


