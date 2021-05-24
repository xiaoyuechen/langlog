:- use_module(library(lists)).
:- use_module(library(pairs)).

walkable(Pos) :-
	black(Pos); food(Pos); treasure(Pos); start(Pos); exit(Pos).

neighbour([X1, Y1], [X2, Y2]) :- X1 =:= X2, (Y1 =:= Y2 - 1; Y1 =:= Y2 + 1).
neighbour([X1, Y1], [X2, Y2]) :- Y1 =:= Y2, (X1 =:= X2 - 1; X1 =:= X2 + 1).

move(From, To) :-
	walkable(From), walkable(To),
	neighbour(From, To).

same([X1, Y1], [X2, Y2]) :- X1 =:= X2, Y1 =:= Y2.

has_food(Pos, EatenList) :- food(Pos), not(member(Pos, EatenList)).

update_energy(Pos, BeginEnergy, _, EatenList, ResultEnergy, ResultEatenList) :-
	has_food(Pos, EatenList),
	ResultEnergy is BeginEnergy - 1,
	ResultEatenList = [Pos | EatenList].
update_energy(_, _, CurrentEnergy, EatenList, ResultEnergy, ResultEatenList) :-
	ResultEnergy is CurrentEnergy - 1,
	ResultEatenList = EatenList.

dfs(From, To, Energy, Path) :-
	dfs_impl(From, To, Energy, Energy, [], [], Path0),
	reverse(Path0, Path).
dfs_impl(From, To, _, Energy, _, Path, [From | Path]) :-
	Energy >= 0,
	same(From, To).
dfs_impl(From, To, BeginEnergy, Energy, EatenList, Path, Sol) :-
	move(From, Next),
	Energy >= 0,
	not(subset([Next, Next, Next, Next], Path)),
	update_energy(From, BeginEnergy, Energy, EatenList, ResultEnergy, ResultEatenList),
	dfs_impl(Next, To, BeginEnergy, ResultEnergy, ResultEatenList, [From | Path], Sol).

shortest(From, To, Energy, Path) :-
	findall(Path0, dfs(From, To, Energy, Path0), Paths),
	map_list_to_pairs(length, Paths, Pairs0),
	keysort(Pairs0, Pairs),
	[_-Path | _] = Pairs.

solve(Energy, Path) :-
	start(S), exit(T),
	shortest(S, T, Energy, Path).
