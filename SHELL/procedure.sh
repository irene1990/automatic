create or replace procedure proc is
begin
  for i in 1 ..100000 loop
    insert into testkk values(i,sysdate,'jsdkfjksdjfskldfj');
    end loop;
end proc;
