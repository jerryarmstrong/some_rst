packages/google_maps_flutter/google_maps_flutter_android/android/src/main/java/io/flutter/plugins/googlemaps/CircleOptionsSink.java
===================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlemaps;

import com.google.android.gms.maps.model.LatLng;

/** Receiver of Circle configuration options. */
interface CircleOptionsSink {

  void setConsumeTapEvents(boolean consumetapEvents);

  void setStrokeColor(int strokeColor);

  void setFillColor(int fillColor);

  void setCenter(LatLng center);

  void setRadius(double radius);

  void setVisible(boolean visible);

  void setStrokeWidth(float strokeWidth);

  void setZIndex(float zIndex);
}


