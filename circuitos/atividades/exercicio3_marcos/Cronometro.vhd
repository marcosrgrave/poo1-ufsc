library ieee;
use ieee.std_logic_1164.all;
use IEEE.std_logic_arith.all; 
use IEEE.std_logic_unsigned.all;

entity Cronometro is port ( 
  CLK1: in std_logic;  -- 1Hz
  CLK2: in std_logic; -- 10Hz
  CLR: in std_logic;  -- KEY(0)
  En : in std_logic;  -- SW(0)
  segmSeg : out std_logic_vector(6 downto 0);
  segmDez : out std_logic_vector(6 downto 0)
  );
end entity;

architecture behv of Cronometro is
--   signal cnt: std_logic_vector(3 downto 0) := "0000";
  signal cntSeg, cntDez : std_logic_vector (3 downto 0);
  signal maxSeg, maxDez : std_logic;
  
  component Contador1 is
    port (
        CLK: in std_logic; -- 1Hz
        CLR: in std_logic; -- KEY(0)
        En : in std_logic; -- SW(0)
        S1: out std_logic_vector(3 downto 0); -- SW(3 downto 0)
        MAX1: out std_logic  -- SW(4)
    );
  end component;
  
  component Contador2 is
    port (
        CLK: in std_logic; -- 1Hz
        CLR: in std_logic; -- KEY(0)
        En : in std_logic; -- SW(0)
        S2: out std_logic_vector(3 downto 0); -- SW(3 downto 0)
        MAX2: out std_logic  -- SW(4)
    );
  end component;
  
  component bcd7seg is
    port(
        bcd_in:  in std_logic_vector(3 downto 0);
        out_7seg:  out std_logic_vector(6 downto 0)
    );
  end component;
  
begin

  Cont1  : Contador1 port map (CLK1,    CLR,    En,     cntSeg, maxSeg);
  Cont2  : Contador2 port map (CLK2,    CLR,    maxSeg, cntDez, maxDez);
  
  BCDSEG : bcd7seg   port map (cntSeg, segmSeg);
  BCDDEZ : bcd7seg   port map (cntDez, segmDez);
  
end architecture;