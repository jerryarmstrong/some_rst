packages/app-mobile/src/features/biometrics/types.ts
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export enum BiometricSettingType {
  RequiredForAppAccess,
  RequiredForTransactions,
}

export interface BiometricSettingsState {
  requiredForAppAccess: boolean;
  requiredForTransactions: boolean;
}

export const initialBiometricsSettingsState: BiometricSettingsState = {
  requiredForAppAccess: false,
  requiredForTransactions: false,
};


