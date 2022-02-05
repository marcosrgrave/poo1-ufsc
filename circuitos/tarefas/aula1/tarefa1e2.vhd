library ieee;
use ieee.std_logic_1164.all;

entity tarefa1 is
    port (
        KEY : in std_logic_vector(3 downto 0);
        SW : in std_logic_vector(3 downto 0);
        LEDR : out std_logic_vector(17 downto 0);
        HEX3 : out std_logic_vector(6 downto 0)  -- cada LED com 7 segmentos
    );
end entity;

architecture rtl of tarefa1 is
    
begin
    
    LEDR(3 downto 0) <= SW(3 downto 0);
    LEDR(17 downto 16) <= KEY(1 downto 0);
    HEX3 <= "0010010";  -- 0 = LED Ligado | 1 = LED Desligado

end architecture;