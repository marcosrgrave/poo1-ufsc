library ieee;
use ieee.std_logic_1164.all;
use IEEE.std_logic_arith.all; 
use IEEE.std_logic_unsigned.all;

entity Contador2 is port ( 
  CLK: in std_logic; -- 1Hz
  CLR: in std_logic; -- KEY(0)
  En : in std_logic; -- SW(0)
  
  S2: out std_logic_vector(3 downto 0); -- SW(3 downto 0)
  MAX2: out std_logic  -- SW(4)
  );
end entity;

architecture behv of Contador2 is
  signal cnt: std_logic_vector(3 downto 0) := "0000";
  signal max, temp_enable : std_logic := '0';
--   signal temp_enable : std_logic;
  
  component bcd7seg is
    port(
        bcd_in:  in std_logic_vector(3 downto 0);
        out_7seg:  out std_logic_vector(6 downto 0)
    );
  end component;
  
begin

  process(CLK,CLR)
  begin
    if (CLR = '0') then
      cnt <= "0000";
      max <= '0';
    elsif (CLK'event and CLK = '1' and En = '1') then 
      if (cnt = "0101") then  -- flag = 5
        cnt <= "0000";
        max <= '1';
      else
        cnt <= cnt + "0001";
        max <= '0';
      end if;
    end if;
  end process;

  S2 <= cnt;
  MAX2 <= max;
  
end architecture;