components/treasuryV2/icons/UnselectedWalletIcon.tsx
====================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import React from 'react'

type Props = React.SVGAttributes<SVGElement>

export default function UnselectedWalletIcon(props: Props) {
  return (
    <svg
      {...props}
      viewBox="0 0 40 40"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M0.5 20C0.5 11.9964 1.51256 7.19455 4.35355 4.35355C7.19455 1.51256 11.9964 0.5 20 0.5C28.0036 0.5 32.8055 1.51256 35.6464 4.35355C38.4874 7.19455 39.5 11.9964 39.5 20C39.5 28.0036 38.4874 32.8055 35.6464 35.6464C32.8055 38.4874 28.0036 39.5 20 39.5C11.9964 39.5 7.19455 38.4874 4.35355 35.6464C1.51256 32.8055 0.5 28.0036 0.5 20Z"
        stroke="white"
        strokeOpacity="0.3"
      />
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="M11 26V14C11 12.3431 12.3431 11 14 11H24.5C25.3284 11 26 11.6716 26 12.5V15.5H27.5C28.3284 15.5 29 16.1716 29 17V27.5C29 28.3284 28.3284 29 27.5 29H14C12.3431 29 11 27.6569 11 26ZM14 15.5C13.1716 15.5 12.5 14.8284 12.5 14C12.5 13.1716 13.1716 12.5 14 12.5H24.5V15.5H14ZM24.5 23C25.3284 23 26 22.3284 26 21.5C26 20.6716 25.3284 20 24.5 20C23.6716 20 23 20.6716 23 21.5C23 22.3284 23.6716 23 24.5 23Z"
        fill="#E5E5E6"
      />
    </svg>
  )
}


