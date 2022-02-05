library ieee;
use ieee.std_logic_1164.all;

entity pablo_led is
port(
    KEY: in std_logic_vector(3 downto 0);
    SW: in std_logic_vector(17 downto 0);
    LEDR: out std_logic_vector(17 downto 0);
    HEX0,HEX1,HEX2,HEX3,HEX4,HEX5,HEX6,HEX7 : out std_logic_vector(6 downto 0)
    );
end pablo_led;

architecture arc of pablo_led is
begin
    LEDR(3 downto 0) <= SW(3 downto 0);
    LEDR(17 downto 16) <= KEY(1 downto 0);
    HEX7 <= "0001100";
    HEX6 <= "0001000";
    HEX5 <= "0000000";
    HEX4 <= "1000111";
    HEX3 <= "1000000";
end arc;
