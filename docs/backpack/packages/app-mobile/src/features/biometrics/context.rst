packages/app-mobile/src/features/biometrics/context.tsx
=======================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import {
  useMemo,
  createContext,
  PropsWithChildren,
  useCallback,
  useContext,
  useState,
} from "react";

import { BiometricAuthenticationStatus } from "~src/features/biometrics/index";

export interface BiometricContextValue {
  authenticationStatus: Maybe<BiometricAuthenticationStatus>;
  setAuthenticationStatus: (
    value: Maybe<BiometricAuthenticationStatus>
  ) => void;
}

const biomericContextValue: BiometricContextValue = {
  authenticationStatus: undefined,
  setAuthenticationStatus: () => undefined,
};

const BiometricContext =
  createContext<BiometricContextValue>(biomericContextValue);

export const BiometricContextProvider = ({
  children,
}: PropsWithChildren<unknown>): JSX.Element => {
  const [status, setStatus] = useState<Maybe<BiometricAuthenticationStatus>>();

  const setAuthenticationStatus = useCallback(
    (value: Maybe<BiometricAuthenticationStatus>): void => {
      setStatus(value);
    },
    [setStatus]
  );

  const contextValue = useMemo(
    () => ({
      authenticationStatus: status,
      setAuthenticationStatus,
    }),
    [status, setAuthenticationStatus]
  );

  return (
    <BiometricContext.Provider value={contextValue}>
      {children}
    </BiometricContext.Provider>
  );
};

export function useBiometricContext(): BiometricContextValue {
  return useContext(BiometricContext);
}


