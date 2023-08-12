packages/webview_flutter/webview_flutter_android/android/src/test/java/io/flutter/plugins/webviewflutter/InstanceManagerTest.java
=================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutter;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class InstanceManagerTest {
  @Test
  public void addDartCreatedInstance() {
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});

    final Object object = new Object();
    instanceManager.addDartCreatedInstance(object, 0);

    assertEquals(object, instanceManager.getInstance(0));
    assertEquals((Long) 0L, instanceManager.getIdentifierForStrongReference(object));
    assertTrue(instanceManager.containsInstance(object));

    instanceManager.close();
  }

  @Test
  public void addHostCreatedInstance() {
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});

    final Object object = new Object();
    long identifier = instanceManager.addHostCreatedInstance(object);

    assertNotNull(instanceManager.getInstance(identifier));
    assertEquals(object, instanceManager.getInstance(identifier));
    assertTrue(instanceManager.containsInstance(object));

    instanceManager.close();
  }

  @Test
  public void remove() {
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});

    Object object = new Object();
    instanceManager.addDartCreatedInstance(object, 0);

    assertEquals(object, instanceManager.remove(0));

    // To allow for object to be garbage collected.
    //noinspection UnusedAssignment
    object = null;

    Runtime.getRuntime().gc();

    assertNull(instanceManager.getInstance(0));

    instanceManager.close();
  }

  @Test
  public void removeReturnsNullWhenClosed() {
    final Object object = new Object();
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});
    instanceManager.addDartCreatedInstance(object, 0);
    instanceManager.close();

    assertNull(instanceManager.remove(0));
  }

  @Test
  public void getIdentifierForStrongReferenceReturnsNullWhenClosed() {
    final Object object = new Object();
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});
    instanceManager.addDartCreatedInstance(object, 0);
    instanceManager.close();

    assertNull(instanceManager.getIdentifierForStrongReference(object));
  }

  @Test
  public void addHostCreatedInstanceReturnsNegativeOneWhenClosed() {
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});
    instanceManager.close();

    assertEquals(instanceManager.addHostCreatedInstance(new Object()), -1L);
  }

  @Test
  public void getInstanceReturnsNullWhenClosed() {
    final Object object = new Object();
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});
    instanceManager.addDartCreatedInstance(object, 0);
    instanceManager.close();

    assertNull(instanceManager.getInstance(0));
  }

  @Test
  public void containsInstanceReturnsFalseWhenClosed() {
    final Object object = new Object();
    final InstanceManager instanceManager = InstanceManager.open(identifier -> {});
    instanceManager.addDartCreatedInstance(object, 0);
    instanceManager.close();

    assertFalse(instanceManager.containsInstance(object));
  }
}


