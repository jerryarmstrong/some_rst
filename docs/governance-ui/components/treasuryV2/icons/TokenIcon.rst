components/treasuryV2/icons/TokenIcon.tsx
=========================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import React from 'react'

type Props = React.SVGAttributes<SVGElement>

export default function TokenIcon(props: Props) {
  return (
    <svg
      {...props}
      viewBox="0 0 16 16"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path d="M13.5 8C13.5 11.0376 11.0376 13.5 8 13.5V14.5C11.5899 14.5 14.5 11.5899 14.5 8H13.5ZM8 13.5C4.96243 13.5 2.5 11.0376 2.5 8H1.5C1.5 11.5899 4.41015 14.5 8 14.5V13.5ZM2.5 8C2.5 4.96243 4.96243 2.5 8 2.5V1.5C4.41015 1.5 1.5 4.41015 1.5 8H2.5ZM8 2.5C11.0376 2.5 13.5 4.96243 13.5 8H14.5C14.5 4.41015 11.5899 1.5 8 1.5V2.5ZM10.5 8C10.5 9.38071 9.38071 10.5 8 10.5V11.5C9.933 11.5 11.5 9.933 11.5 8H10.5ZM8 10.5C6.61929 10.5 5.5 9.38071 5.5 8H4.5C4.5 9.933 6.067 11.5 8 11.5V10.5ZM5.5 8C5.5 6.61929 6.61929 5.5 8 5.5V4.5C6.067 4.5 4.5 6.067 4.5 8H5.5ZM8 5.5C9.38071 5.5 10.5 6.61929 10.5 8H11.5C11.5 6.067 9.933 4.5 8 4.5V5.5Z" />
    </svg>
  )
}


