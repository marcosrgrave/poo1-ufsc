library ieee;
use ieee.std_logic_1164.all;
use IEEE.std_logic_arith.all; 
use IEEE.std_logic_unsigned.all;

entity Conta4 is port ( 
  CLK: in std_logic;
  CLR: in std_logic;
  S: out std_logic_vector(3 downto 0) );
end Conta4;

architecture behv of Conta4 is
  signal cnt: std_logic_vector(3 downto 0) := "0000";
begin

  process(CLK,CLR)
  begin
    if (CLR = '1') then
      cnt <= "0000";
    elsif (CLK'event and CLK = '1') then 
      cnt <= cnt + "0001";
    end if;
  end process;

  S <= cnt;

end behv;