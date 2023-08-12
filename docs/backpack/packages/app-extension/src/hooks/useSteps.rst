packages/app-extension/src/hooks/useSteps.tsx
=============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useState } from "react";

export const useSteps = () => {
  const [step, setStep] = useState(0);
  const nextStep = () => setStep(step + 1);
  const prevStep = () => {
    if (step > 0) setStep(step - 1);
  };

  return {
    step,
    setStep,
    nextStep,
    prevStep,
  };
};


