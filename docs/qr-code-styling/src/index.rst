src/index.ts
============

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: ts

    import QRCodeStyling from "./core/QRCodeStyling";
import dotTypes from "./constants/dotTypes";
import cornerDotTypes from "./constants/cornerDotTypes";
import cornerSquareTypes from "./constants/cornerSquareTypes";
import errorCorrectionLevels from "./constants/errorCorrectionLevels";
import errorCorrectionPercents from "./constants/errorCorrectionPercents";
import modes from "./constants/modes";
import qrTypes from "./constants/qrTypes";
import drawTypes from "./constants/drawTypes";
import shapeTypes from "./constants/shapeTypes";
import gradientTypes from "./constants/gradientTypes";

export * from "./types";

export {
  dotTypes,
  cornerDotTypes,
  cornerSquareTypes,
  errorCorrectionLevels,
  errorCorrectionPercents,
  modes,
  qrTypes,
  drawTypes,
  shapeTypes,
  gradientTypes
};

export default QRCodeStyling;


