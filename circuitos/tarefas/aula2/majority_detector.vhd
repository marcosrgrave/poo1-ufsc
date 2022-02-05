-- Libraries and Packages (IEEE)
library ieee;
use ieee.std_logic_1164.all;

-- Entity (Ports)
entity majority_detector is
    port (
        A, B, C : in std_logic;
        Y : out std_logic  -- na ultima porta não vai ';' no final.
    );
end entity;

-- Architecture (Comportamento/Funcionalidade)
architecture rtl of majority_detector is
    -- no signals declared for this entity
begin    
    Y <= (A and B) or (A and C) or (B and C);
    -- precisa mapear as portas no 'Mapper' do FPGAEmuWeb (UFSC)
    -- caso queira mapear no proprio codigo, basta:
    --    1. definir apenas as portas SW (2 downto 0) e LEDR (std_logic), sem as portas A, B, C e Y
    --    2. definir A, B, C e Y como signals
    --    3. definir A <= SW(0); B <= SW(1); C <= SW(2); LEDR <= Y
end architecture;