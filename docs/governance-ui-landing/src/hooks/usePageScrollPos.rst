src/hooks/usePageScrollPos.ts
=============================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: ts

    import { throttle } from 'lodash';
import { useEffect, useState } from 'react';

export default function usePageScrollPos() {
  const [pos, setPos] = useState(0);

  useEffect(() => {
    const handleScroll = throttle(() => {
      setPos(window.scrollY);
    }, 16);

    window.addEventListener('scroll', handleScroll);

    handleScroll();

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return pos;
}


