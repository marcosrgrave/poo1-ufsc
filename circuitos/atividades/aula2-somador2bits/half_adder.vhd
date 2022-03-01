-- Libraries and Packages (IEEE)
library ieee;
use ieee.std_logic_1164.all;

-- Entity (Ports)
entity half_adder is
    port (
        A, B : in std_logic;
        S, Cout : out std_logic
    );
end entity;

-- Architecture (Comportamento/Funcionalidade)
architecture rtl of half_adder is
    -- no signals declared for this entity
begin    
    S <= A xor B;
    Cout <= A and B;
end architecture;