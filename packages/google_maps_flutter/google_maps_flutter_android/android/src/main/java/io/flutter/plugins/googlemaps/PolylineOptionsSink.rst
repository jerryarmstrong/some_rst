packages/google_maps_flutter/google_maps_flutter_android/android/src/main/java/io/flutter/plugins/googlemaps/PolylineOptionsSink.java
=====================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlemaps;

import com.google.android.gms.maps.model.Cap;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.PatternItem;
import java.util.List;

/** Receiver of Polyline configuration options. */
interface PolylineOptionsSink {

  void setConsumeTapEvents(boolean consumetapEvents);

  void setColor(int color);

  void setEndCap(Cap endCap);

  void setGeodesic(boolean geodesic);

  void setJointType(int jointType);

  void setPattern(List<PatternItem> pattern);

  void setPoints(List<LatLng> points);

  void setStartCap(Cap startCap);

  void setVisible(boolean visible);

  void setWidth(float width);

  void setZIndex(float zIndex);
}


