packages/google_maps_flutter/google_maps_flutter_android/android/src/main/java/io/flutter/plugins/googlemaps/PolygonOptionsSink.java
====================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlemaps;

import com.google.android.gms.maps.model.LatLng;
import java.util.List;

/** Receiver of Polygon configuration options. */
interface PolygonOptionsSink {

  void setConsumeTapEvents(boolean consumetapEvents);

  void setFillColor(int color);

  void setStrokeColor(int color);

  void setGeodesic(boolean geodesic);

  void setPoints(List<LatLng> points);

  void setHoles(List<List<LatLng>> holes);

  void setVisible(boolean visible);

  void setStrokeWidth(float width);

  void setZIndex(float zIndex);
}


