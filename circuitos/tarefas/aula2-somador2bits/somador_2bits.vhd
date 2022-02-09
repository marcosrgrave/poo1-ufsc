-- SOMADOR 2 BITS: half_adder + full_adder

-- Libraries and Packages (IEEE)
library ieee;
use ieee.std_logic_1164.all;

-- Entity (Ports)
entity somador_2bits is
    port (
        A0, A1, B0, B1 : in std_logic;
        S0, S1, S2 : out std_logic
    );
end entity;

-- Architecture (Comportamento/Funcionalidade)
architecture rtl of somador_2bits is
    signal half_and, full_xor1 : std_logic;
begin    
    -- portas do half_adder
    S0 <= A0 xor B0;
    half_and <= A0 and B0;
    
    -- portas do full_adder
    full_xor1 <= A1 xor B1;
    S1 <= full_xor1 xor half_and;
    S2 <= (half_and and full_xor1) or (A1 and B1);
end architecture;