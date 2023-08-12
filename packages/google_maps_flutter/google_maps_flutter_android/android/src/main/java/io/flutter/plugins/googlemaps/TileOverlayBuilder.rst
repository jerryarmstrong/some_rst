packages/google_maps_flutter/google_maps_flutter_android/android/src/main/java/io/flutter/plugins/googlemaps/TileOverlayBuilder.java
====================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.googlemaps;

import com.google.android.gms.maps.model.TileOverlayOptions;
import com.google.android.gms.maps.model.TileProvider;

class TileOverlayBuilder implements TileOverlaySink {

  private final TileOverlayOptions tileOverlayOptions;

  TileOverlayBuilder() {
    this.tileOverlayOptions = new TileOverlayOptions();
  }

  TileOverlayOptions build() {
    return tileOverlayOptions;
  }

  @Override
  public void setFadeIn(boolean fadeIn) {
    tileOverlayOptions.fadeIn(fadeIn);
  }

  @Override
  public void setTransparency(float transparency) {
    tileOverlayOptions.transparency(transparency);
  }

  @Override
  public void setZIndex(float zIndex) {
    tileOverlayOptions.zIndex(zIndex);
  }

  @Override
  public void setVisible(boolean visible) {
    tileOverlayOptions.visible(visible);
  }

  @Override
  public void setTileProvider(TileProvider tileProvider) {
    tileOverlayOptions.tileProvider(tileProvider);
  }
}


