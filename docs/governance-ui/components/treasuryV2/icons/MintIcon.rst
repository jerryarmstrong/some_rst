components/treasuryV2/icons/MintIcon.tsx
========================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import React from 'react'

type Props = React.SVGAttributes<SVGElement>

export default function MintIcon(props: Props) {
  return (
    <svg
      {...props}
      viewBox="0 0 16 16"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path d="M8 14.0003C4.5 14.0003 2 12.9687 2 11.9491V9.17969C2 10.4104 4.5 11.4361 8 11.4361C11.5 11.4361 14 10.4104 14 9.17969V11.9491C14 12.9687 11.5 14.0003 8 14.0003Z" />
      <path d="M2 9.17954V6.41016C2 7.6409 4.5 8.66653 8 8.66653C11.5 8.66653 14 7.6409 14 6.41016V9.17954" />
      <path d="M14 3.84612C14 2.61537 11.5 2 8 2C4.5 2 2 2.61537 2 3.84612M14 3.84612V6.61531C14 7.63489 11.5 8.66656 8 8.66656C4.5 8.66656 2 7.63489 2 6.61531V3.84612M14 3.84612C14 5.07687 11.5 6.1025 8 6.1025C4.5 6.1025 2 5.07687 2 3.84612" />
    </svg>
  )
}


