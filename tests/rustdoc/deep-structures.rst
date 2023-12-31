tests/rustdoc/deep-structures.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test verifies that we do not hit recursion limit trying to prove auto-trait bounds for
// reasonably deep structures.

#![crate_type="rlib"]

pub struct A01(A02);
pub struct A02(A03);
pub struct A03(A04);
pub struct A04(A05);
pub struct A05(A06);
pub struct A06(A07);
pub struct A07(A08);
pub struct A08(A09);
pub struct A09(A10);
pub struct A10(A11);
pub struct A11(A12);
pub struct A12(A13);
pub struct A13(A14);
pub struct A14(A15);
pub struct A15(A16);
pub struct A16(A17);
pub struct A17(A18);
pub struct A18(A19);
pub struct A19(A20);
pub struct A20(A21);
pub struct A21(A22);
pub struct A22(A23);
pub struct A23(A24);
pub struct A24(A25);
pub struct A25(A26);
pub struct A26(A27);
pub struct A27(A28);
pub struct A28(A29);
pub struct A29(A30);
pub struct A30(A31);
pub struct A31(A32);
pub struct A32(A33);
pub struct A33(A34);
pub struct A34(A35);
pub struct A35(A36);
pub struct A36(A37);
pub struct A37(A38);
pub struct A38(A39);
pub struct A39(A40);
pub struct A40(A41);
pub struct A41(A42);
pub struct A42(A43);
pub struct A43(A44);
pub struct A44(A45);
pub struct A45(A46);
pub struct A46(A47);
pub struct A47(A48);
pub struct A48(A49);
pub struct A49(A50);
pub struct A50(A51);
pub struct A51(A52);
pub struct A52(A53);
pub struct A53(A54);
pub struct A54(A55);
pub struct A55(A56);
pub struct A56(A57);
pub struct A57(A58);
pub struct A58(A59);
pub struct A59(A60);
pub struct A60(A61);
pub struct A61(A62);
pub struct A62(A63);
pub struct A63(A64);
pub struct A64(A65);
pub struct A65(A66);
pub struct A66(A67);
pub struct A67(A68);
pub struct A68(A69);
pub struct A69(A70);
pub struct A70(A71);
pub struct A71(A72);
pub struct A72(A73);
pub struct A73(A74);
pub struct A74(A75);
pub struct A75(A76);
pub struct A76(A77);
pub struct A77(A78);
pub struct A78(A79);
pub struct A79(A80);
pub struct A80(A81);
pub struct A81(A82);
pub struct A82(A83);
pub struct A83(A84);
pub struct A84(A85);
pub struct A85(A86);
pub struct A86(A87);
pub struct A87(A88);
pub struct A88(A89);
pub struct A89(A90);
pub struct A90(A91);
pub struct A91(A92);
pub struct A92(A93);
pub struct A93(A94);
pub struct A94(A95);
pub struct A95(A96);
pub struct A96(A97);
pub struct A97(A98);
pub struct A98(A99);
pub struct A99;


