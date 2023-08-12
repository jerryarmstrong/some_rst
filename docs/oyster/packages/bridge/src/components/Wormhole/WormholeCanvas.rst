packages/bridge/src/components/Wormhole/WormholeCanvas.tsx
==========================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import * as React from 'react';
import { Canvas } from 'react-three-fiber';
import Camera from './Camera';
import WormholeGeometry from './WormholeGeometry';

/**
 * Three.js wormhole component.
 *
 * @returns {JSX.Element}
 * @constructor
 */
const WormholeCanvas = ({
  onCreated,
  rotate,
}: {
  onCreated: any;
  rotate?: boolean;
}) => {
  return (
    <Canvas onCreated={onCreated} style={{ opacity: 0.4 }}>
      <Camera />
      <React.Suspense fallback={null}>
        <WormholeGeometry rotate={rotate} />
      </React.Suspense>
    </Canvas>
  );
};

export default WormholeCanvas;


