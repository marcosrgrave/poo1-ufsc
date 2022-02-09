-- Libraries and Packages (IEEE)
library ieee;
use ieee.std_logic_1164.all;

-- Entity (Ports)
entity full_adder is
    port (
        A, B, Cin : in std_logic;
        S, Cout : out std_logic
    );
end entity;

-- Architecture (Comportamento/Funcionalidade)
architecture rtl of full_adder is
    -- no signals declared for this entity
begin    
    S <= (A xor B) xor Cin;
    Cout <= ((A xor B) and Cin) or (A and B);
end architecture;