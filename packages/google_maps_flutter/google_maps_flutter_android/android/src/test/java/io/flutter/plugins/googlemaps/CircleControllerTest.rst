packages/google_maps_flutter/google_maps_flutter_android/android/src/test/java/io/flutter/plugins/googlemaps/CircleControllerTest.java
======================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlemaps;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;

import com.google.android.gms.internal.maps.zzl;
import com.google.android.gms.maps.model.Circle;
import org.junit.Test;
import org.mockito.Mockito;

public class CircleControllerTest {

  @Test
  public void controller_SetsStrokeDensity() {
    final zzl z = mock(zzl.class);
    final Circle circle = spy(new Circle(z));

    final float density = 5;
    final float strokeWidth = 3;
    final CircleController controller = new CircleController(circle, false, density);
    controller.setStrokeWidth(strokeWidth);

    Mockito.verify(circle).setStrokeWidth(density * strokeWidth);
  }
}


