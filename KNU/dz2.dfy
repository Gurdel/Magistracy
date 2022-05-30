class {:autocontracts} Turnstile
{
    var users: array<int>;
    var usersCount: int;
    var isOpened: bool;

    predicate Valid() {
       users.Length != 0 && 0 <= usersCount <= users.Length
    }

    constructor ()
    ensures usersCount == 0
    {
        users, usersCount, isOpened := new int[10], 0, false;
    }


    method AddUser(d: int)
    {
        print "AddUser   ";
        var userExists := UserExists(d);
        if (!userExists)
        {
            if usersCount == users.Length {
                var b := new int[2 * users.Length]; 
                forall (i | 0 <= i < usersCount) 
                {
                    b[i] := users[i];
                }
                users := b;
            }

            users[usersCount], usersCount := d, usersCount + 1;
        }
        else
        {
           print "  user already exists\n";
        }

        var i := 0;
        while (i < usersCount)
        {
            print users[i], " ";
            i := i + 1;
        }
        print usersCount, "\n";
    }


    method UserExists(key: int) returns (res: bool)
    ensures usersCount == 0 ==> res == false;
    ensures (forall i :: 0 <= i < usersCount && users[i]!=key) ==> res == false;
    {
        print "UserExists(", key, "):";
        if usersCount == 0
        {
            res := false;
            print res, "\n";
            return; 
        }
        var index := 0;
        while (index < usersCount)
        invariant 0 <= index <= users.Length;
        {
            if (users[index] == key) 
            { 
                res := true;
                print res, "\n";
                return; 
            }
            index := index + 1;
        }
        res := false;
        print res, "\n";
    }


    method ReadUserCard(userId: int) returns (isUserPermitted: bool)
    ensures old(isOpened) ==> isOpened == old(isOpened);
    ensures !old(isOpened) && isUserPermitted ==> isOpened == true
    {
        print "ReadUserCard   ";
        if (isOpened)
        {
            print "   already opened\n";
            return;
        }
        
        isUserPermitted := UserExists(userId);

        if (isUserPermitted)
        {
            isOpened := true;
            print "   opened\n";
            return;
        }
        print "   wrong user, not opened\n";
    }


    method TryGo() returns (res: bool)
    ensures !old(isOpened) ==> isOpened == old(isOpened)
    ensures old(isOpened) ==> isOpened == !old(isOpened)
    {
        print "TryGo    ";
        if (!isOpened)
        {
            print "can't enter - turnstile is closed\n";
            res := false;
            return;
        }

        isOpened := false;
        res := true;
        print "user entered, now turnstile is closed again\n";
    }
}


method Main()
{ 
    var turn := new Turnstile();
    turn.AddUser(1);
    turn.AddUser(3);
    turn.AddUser(3);

    var buf := turn.ReadUserCard(1);
    var res1 := turn.TryGo();
    print res1,"\n";
    var res2 := turn.TryGo();
    print res2,"\n";
    buf := turn.ReadUserCard(3);
    var res3 := turn.TryGo();
    print res3,"\n";
}
