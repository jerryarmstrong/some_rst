packages/metavinci/src/components/ArtContent/index.tsx
======================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React, { useMemo } from 'react';
import { Image } from 'antd';
import { MetadataCategory } from '@oyster/common'

export const ArtContent = ({
  content,
  category,
  className,
  preview
 }: {
    category?: MetadataCategory,
    content?: string,
    className?: string,
    preview?: boolean,
  }) => {
  return category === 'video' ?
    <video src={content}
           className={className}
           playsInline={true}
           autoPlay={true}
           controlsList="nodownload"
           loop={true} /> :
    <Image
      src={content}
      preview={preview}
      wrapperClassName={className}
    />;
}


