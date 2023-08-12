packages/google_maps_flutter/google_maps_flutter_android/android/src/test/java/io/flutter/plugins/googlemaps/CircleBuilderTest.java
===================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlemaps;

import static junit.framework.TestCase.assertEquals;

import com.google.android.gms.maps.model.CircleOptions;
import org.junit.Test;

public class CircleBuilderTest {

  @Test
  public void density_AppliesToStrokeWidth() {
    final float density = 5;
    final float strokeWidth = 3;
    final CircleBuilder builder = new CircleBuilder(density);
    builder.setStrokeWidth(strokeWidth);

    final CircleOptions options = builder.build();
    final float width = options.getStrokeWidth();

    assertEquals(density * strokeWidth, width);
  }
}


