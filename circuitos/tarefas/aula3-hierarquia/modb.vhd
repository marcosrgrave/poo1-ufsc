library ieee;
use ieee.std_logic_1164.all;

entity modb is
    port (
        C0, C1, B : in std_logic;
        S : out std_logic
    );
end entity;

architecture rtl of modb is
    -- no signal or component
begin
    
    S <= (C1 and not B) or (not C0 and B);

end architecture;