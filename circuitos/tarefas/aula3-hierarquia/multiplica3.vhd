library ieee;
use ieee.std_logic_1164.all;

entity multiplica3 is  -- o intuito é somar 3x o mesmo numero, que é o mesmo que multiplicar por 3
    port (
        numero_multiplicado : in std_logic_vector (3 downto 0); -- numero de 4 bits
        resultado_multiplicacao : out std_logic_vector (4 downto 0)  -- resultado de 5 bits
    );
end entity;

architecture tanto_faz of multiplica3 is
    
    signal resultado_soma1 : std_logic_vector (4 downto 0);
    
    component somador4bits is
        port(
            A, B : in std_logic_vector (3 downto 0);  -- 2 numeros de 4 bits que serao somados
            S : out std_logic_vector (4 downto 0)  -- saida = 1 numero de 5 bits
        );
    end component;

begin
    
    SOMA1 : somador4bits port map (  -- somando X com X
        numero_multiplicado,
        numero_multiplicado,
        resultado_soma1
        );
    
    SOMA2 : somador4bits port map ( -- somando X com (X+X)
        numero_multiplicado, 
        resultado_soma1 (3 downto 0), -- para evitar erro quando a soma retornar 5 bits
        resultado_multiplicacao
        );

end architecture;